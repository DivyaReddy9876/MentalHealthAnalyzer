import tkinter as tk
from tkinter import ttk, scrolledtext
import re

class MentalHealthAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mental Health Analysis")
        self.geometry("600x800")

        # Keywords for analysis
        self.positive_keywords = {
            'happy': 0.8, 'grateful': 0.9, 'excited': 0.7, 'peaceful': 0.8, 'loved': 0.9,
            'accomplished': 0.8, 'confident': 0.7, 'inspired': 0.7, 'relaxed': 0.6
        }
        
        self.negative_keywords = {
            'sad': -0.7, 'anxious': -0.8, 'stressed': -0.7, 'overwhelmed': -0.9,
            'depressed': -0.9, 'angry': -0.7, 'tired': -0.5, 'worried': -0.6,
            'lonely': -0.8
        }

        self.create_widgets()

    def create_widgets(self):
        # Input frame
        input_frame = ttk.LabelFrame(self, text="Enter your statement:")
        input_frame.pack(padx=10, pady=5, fill="x")

        self.text_input = scrolledtext.ScrolledText(input_frame, height=4)
        self.text_input.pack(padx=5, pady=5, fill="x")

        # Analyze button
        self.analyze_button = ttk.Button(self, text="Analyze", command=self.analyze_text)
        self.analyze_button.pack(pady=10)

        # Results frame
        results_frame = ttk.LabelFrame(self, text="Analysis Results")
        results_frame.pack(padx=10, pady=5, fill="x")

        self.result_text = scrolledtext.ScrolledText(results_frame, height=8)
        self.result_text.pack(padx=5, pady=5, fill="x")

        # Example statements frame
        examples_frame = ttk.LabelFrame(self, text="Example Statements")
        examples_frame.pack(padx=10, pady=5, fill="x")

        examples = [
            "I'm feeling happy and grateful today",
            "I've been feeling overwhelmed lately",
            "I'm excited about my future",
            "I'm having trouble sleeping and feeling anxious",
            "I feel peaceful and relaxed"
        ]

        for example in examples:
            ttk.Label(examples_frame, text=f"• {example}").pack(anchor="w", padx=5, pady=2)

    def analyze_text(self):
        text = self.text_input.get("1.0", "end-1c").lower()
        
        # Calculate sentiment scores
        positive_score = sum(weight for word, weight in self.positive_keywords.items() if word in text)
        negative_score = sum(weight for word, weight in self.negative_keywords.items() if word in text)
        
        # Calculate overall score
        overall_score = positive_score + negative_score
        
        # Determine category and confidence
        if overall_score > 0.3:
            category = "Positive"
            confidence = min(abs(overall_score * 100), 100)
            recommendations = [
                "• Continue maintaining your positive mindset",
                "• Share your positive energy with others",
                "• Document your positive experiences in a journal",
                "• Set new goals to maintain momentum"
            ]
        elif overall_score < -0.3:
            category = "Concerning"
            confidence = min(abs(overall_score * 100), 100)
            recommendations = [
                "• Consider seeking professional help",
                "• Practice regular self-care activities",
                "• Talk to trusted friends or family",
                "• Try relaxation techniques or meditation"
            ]
        else:
            category = "Neutral"
            confidence = min(abs(overall_score * 100), 100)
            recommendations = [
                "• Monitor your feelings regularly",
                "• Practice mindfulness",
                "• Maintain a balanced routine",
                "• Engage in activities you enjoy"
            ]

        # Update results
        self.result_text.delete("1.0", tk.END)
        results = f"Category: {category}\n"
        results += f"Confidence: {confidence:.1f}%\n\n"
        results += "Recommendations:\n"
        results += "\n".join(recommendations)
        
        self.result_text.insert("1.0", results)

if __name__ == "__main__":
    app = MentalHealthAnalyzer()
    app.mainloop()
